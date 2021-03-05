apt update && apt install -y python python-pip
pip install gradescope-utils>=0.3.1 boto3 google-cloud-storage azure-storage-blob

cd /autograder
git clone https://github.com/chiache/csce678-s21-project1 grading
cp /autograder/source/run_tests.py /autograder/grading/run_tests.py

cd /autograder/grading
git submodule update --init
