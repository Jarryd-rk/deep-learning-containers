# Please only set it to True if you are preparing a Benchmark related PR
# Do remember to revert it back to False before merging any PR (including Benchmark dedicated PR)
ENABLE_BENCHMARK_DEV_MODE = True
# Disable the test codebuild jobs to be run
DISABLE_SANITY_TESTS = False
DISABLE_SAGEMAKER_TESTS = False
DISABLE_ECS_TESTS = False
DISABLE_EKS_TESTS = False
DISABLE_EC2_TESTS = False
USE_SCHEDULER = False
