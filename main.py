# This is the main Python script executing Function(s)/Module(s) as required for the Application to run

# Main function
def main():
    import Modules.run_facebook

    Modules.run_facebook.start_facebook_application("dev")

# Main execution
if __name__ == "__main__":
    main()