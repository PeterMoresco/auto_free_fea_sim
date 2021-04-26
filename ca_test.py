#!/usr/bin/env python3

import subprocess
import time
import os
import getpass
import click

@click.command()
@click.option('--install', '-i',
        type=click.Choice(['salome-meca', 'code-aster', 'code-aster-parallel'], case_sensitive=True),
        help='Define the type of installation to run the tests')
@click.option('--max_count', '-mc',
        default=0, help='Number of test cases to run')
def run_test(install, max_count):
    '''
    This script run the test cases for Code Aster.
    '''
    # Define the 'AS_RUN' string
    as_run = AS_RUN(install)
    click.echo(click.style('Found the Code Aster as_run\n {}'.format(as_run),
        fg='yellow'))
    # Create temp dir
    tmp_dir = TMP_DIR()
    click.echo(click.style('Create the test dir in\n {}'.format(tmp_dir),
        fg='yellow'))
    # Enter the test dir
    os.chdir(tmp_dir)
    # Get the testcases
    test_cases = TEST_CASES(install, as_run, tmp_dir)
    # Run the testcases
    RUN_TEST(as_run, tmp_dir, test_cases, max_count)
    # Diagnose the results
    

def AS_RUN(ins):
    userlogin = getpass.getuser()
    if ins == 'salome-meca':
        # Compose path string
        sm_path = ''.join(['/home/', userlogin, '/salome_meca/'])
        if not os.path.exists(sm_path):
            raise Exception('The path to salome "{}" doesnt exists'.format(sm_path))
        else:
            # Try to find the appli folder
            for l in os.listdir(sm_path):
                if l.startswith('appli'):
                    run_path = sm_path  + l + '/salome'
                    break
            else:
                raise Exception('The salome appli folder was not found')
            if not os.path.exists(run_path):
                raise Exception('The salome run script was not found in "{}"'.format(run_path))
            else:
                # Returns the string to run Code Aster as_run
                # From Salome Meca as a shell
                return run_path + ' shell -- as_run'
    elif ins == 'code-aster' or ins == 'code-aster-parallel':
        ca_path = ''.join(['/home/', userlogin, '/aster/bin/as_run'])
        if not os.path.exists(ca_path):
            raise Exception('The Code Aster as_run was not found in "{}"'.format(ca_path))
        else:
            return ca_path

def TMP_DIR():
    try:
        userlogin = getpass.getuser()
        tmp_dir = '/home/' + userlogin + '/test/'
        # Check if the test dir exists
        if not os.path.exists(tmp_dir):
            os.mkdir(tmp_dir)
        else:
            for f in os.listdir(tmp_dir):
                os.remove(tmp_dir + f)
        return tmp_dir
    except OSError:
        raise OSError("The dir {} couldn't  be created".format(tmp_dir))

def TEST_CASES(install, as_run, tmp_dir):
    # Check if the testcases file exists
    # And remove it if it does
    test_cases = tmp_dir + 'testcases'
    if os.path.exists(test_cases):
        os.remove(test_cases)
    #Salome Meca string
    if install == 'code-aster-parallel':
        os.system('''{} --list --all --filter='"parallel" in testlist' --output={} > /dev/null'''.format(as_run, test_cases))
    else:
        # '> /dev/null' makes the stdout not show in the screen
        os.system('{} --list --all --output={} > /dev/null'.format(as_run, test_cases))
    return test_cases

def RUN_TEST(as_run, tmp_dir, testcases, m_count):
    # Open the testcases file and retrieve the test files
    with open(testcases, 'r') as f:
        tests = f.readlines()
    COUNT = len(tests)

    if m_count > COUNT:
        click.echo(click.style('The max_count {} is bigger than the tests found {}. The max_count will be {}'.format(m_count, COUNT, COUNT), fg='magenta'))
    click.echo(click.style('Found {} testcases'.format(COUNT), fg='cyan'))

    if m_count < COUNT and m_count != 0:
        click.echo(click.style('{} tests will be run'.format(m_count), fg='cyan'))
        COUNT = m_count

    # Initiate the time countdown for the test
    INIT = time.time()

    # Loop trough the testcases
    for i, test in enumerate(tests):
        # Checks the boundaries
        if i > COUNT:
            break

        click.echo(click.style('Working on {}, {} of {} ({:.2f}%)\r'.format(test.strip(), i, COUNT,i/COUNT * 100), fg='blue'), nl=False)
        if install == 'code-aster-parallel':
            run_str = '{} --vers stable_mpi --test {} {} >> {}screen'.format(as_run, test.strip(), tmp_dir, tmp_dir)
        else:
            run_str = '{} --test {} {} >> {}screen'.format(as_run, test.strip(), tmp_dir, tmp_dir)
        subprocess.run([run_str], shell=True)

    click.echo(click.style('The tests took {:.2f} minutes to run                             '.format((time.time() - INIT)/60), 
        fg='cyan'))
    return 0

if __name__ == '__main__':
    run_test()
