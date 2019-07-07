import sys
import os
import subprocess
import matplotlib
import unittest

matplotlib.use('Agg')

script_dir = os.path.sep.join(
    os.path.abspath(__file__).split(os.path.sep)[:-2] + ['examples']
)

def test_scripts(script_dir=script_dir):

    passing = []

    for dirname, _, filenames in os.walk(script_dir):
        for filename in filenames:
            if filename.endswith(".py"):

                testme = dirname + os.path.sep + filename
                print("\n------ Testing {} --------- \n".format(filename))

                try:
                    exc = subprocess.check_call(['python', testme])
                    print("  ... {} Passed \n".format(filename))
                    passing += [True]
                except subprocess.CalledProcessError as exc:
                    passing += [False]

                    msg = "\n ... {} FAILED \n".format(filename)

                    traceback = """
        ----------------- >> begin Traceback << ----------------- \n
        {}\n{}\n
        \n----------------- >> end Traceback << -----------------\n
                    """.format(
                        exc.returncode, exc.output
                    )
                    print(u"{}".format(msg + traceback))

    assert all(passing)


# tests = TestScripts(directory=script_dir)
# print(Test._script_path)
# TestScripts = Test.get_tests()
# tests.run_tests()
# unittest.main()
