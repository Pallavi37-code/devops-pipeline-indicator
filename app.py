
def get_pipeline_status(test_passed):
    if test_passed:
        return "SUCCESS"
    return "FAILURE"


if __name__ == "__main__":
    print("DevOps Pipeline Success Indicator")
    print("Current status:", get_pipeline_status(True))
