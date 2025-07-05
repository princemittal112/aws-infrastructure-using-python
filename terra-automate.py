import subprocess

def terraform_command_live(command):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    for line in process.stdout:
        print(line.strip()) 

    process.wait()
    print(f"\n Command finished with exit code: {process.returncode}")

directory = "/Users/princemittal/terraform/variables" # copy path of terraform directory to automate

print(" Initializing Terraform...")
terraform_command_live(f"terraform -chdir={directory} init")

print("\n Applying Terraform...")
terraform_command_live(f"terraform -chdir={directory} apply -auto-approve")

# print("\n Destroying Terraform resources...")
# terraform_command_live(f"terraform -chdir={directory} destroy -auto-approve")
