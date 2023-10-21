############### I M P O R T A N T ###############
#Install boto3 $pip install boto3
#Install awscli $sudo apt install awscli
#Use Environment Variables for Access Key $export AWS_ACCESS_KEY_ID=<YOUR_ACCESS_KEY>
#Use Environment Variables for Secret Key $export AWS_SECRET_ACCESS_KEY=<YOUR_SECRET_KEY>
#$sudo aws configure
#You will need AWS Access Key ID & AWS Secret Access Key
#Default Region us-east-1
#Default output format: json

################## I M P O R T - M O D U L E S ################
import csv
import boto3

############### F U N C T I O N - T O - L I S T - I A M - P O L I C I E S ###############
# Define a function that will list IAM policies:
def list_iam_policies():
    # Declare a variable for the created IAM client
    client = boto3.client('iam')

    # Declare a variable that stores the dictionary of IAM policies to be used later
    response = client.list_policies()

    # Declare a variable that will store the extracted list of policies from the IAM policies,
    # which was stored in a variable "response".
    # This variable contains a list that will be iterated through in another function later
    policies = response['Policies']

    # The value in the variable "policies"
    # to be returned to the function caller
    # in another function later
    return policies

############### F U N C T I O N - T O - W R I T E - I A M - P O L I C I E S - T O - F I L E ###############
# Define a function to write IAM policies to a CSV file
def write_policies_to_csv(policies, csv_filename):
    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='') as csvfile:
        # Declare a variable for the name of the CSV file
        file_name = 'IAM_policies.csv'

        # Declare a variable to store the list of header_names
        header_names = ['Policy Name', 'PolicyId', 'Arn']

        # Create a CSV writer with the file_name and header_names
        writer = csv.DictWriter(csvfile, fieldnames=header_names)

        # First write will create the CSV file and write the header_names to the CSV file
        writer.writeheader()

        # Iterate through IAM policies
        for policy in policies:
            # Write each policy as a row in the CSV
            writer.writerow({
                # FORMAT:
                # <csv_header_names>:
                # <policy is each element in the list policies>
                # [<For each element, grab the value of the corresponding value of the associated key from the policies dictionary>]
                'Policy Name': policy['PolicyName'],
                'PolicyId': policy['PolicyId'],
                'Arn': policy['Arn']
            })

############### C A L L - T H E - F U N C T I O N ###############
# This line checks if the script is being run in the main script or being imported as a module.
# If this is the main script, then execute the code.
# If this is not the main script, then import the function but not execute it
if __name__ == "__main__":
    # Call the "list_iam_policies" function to retrieve the list of IAM policies and store it in a variable
    policies = list_iam_policies()

    # Specify the CSV filename
    csv_filename = 'IAM_policies.csv'

    # Call the "write_policies_to_csv" function, passing the policies list and filename
    write_policies_to_csv(policies, csv_filename)
