#Using IAM boto3.clientLinks to an external site., 
#create a function that iterates through a dictionary of IAM policies to 
#create a CSV file with 
#a row for each policy with the 
#columns 'Policy Name', 'PolicyId', and 'Arn'.


import csv
import boto3
############### F U N C T I O N - T O - L I S T - I A M - P O L I C I E S ###############
#Define a function that will:
def list_iam_policies():

    #Declare a variable for the IAM client
    client = boto3.client('iam')

    #Declare a variable that stores the list of IAM policies to be used later
    response = client.list_policies()

    #Declare a variable that will store the extracted list of policies from the IAM policies, 
    #which was stored in a variable "repsonse".
    #This variable containing a list will be iterated through in a another function later
    policies = response['Policies']

    #the value in the variable "policies" 
    #to be returned to the function caller 
    #in another function later
    return policies


#########################################################

def write_policies_to_csv(policies, csv_filename):

    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='') as csvfile:
	
	#Declare a variable for the name of the csv file
	file_name = 'IAM_Policies.csv'

	#Declare a variable to store the list of header_names
        header_names = ['Policy Name', 'PolicyId', 'Arn']
        
        #Declare a variable that has the CSV writer created with the file_name and header_names passed to it to be used later 
        writer = csv.DictWriter(file_name, fieldnames=header_names)


        #First write will create the csv file and write the header_names to the csv file
        writer.writeheader()


#################### T U R N - T H I S - T O - A - F U N c t I O N    ##########
        
        # Iterate through the IAM policies and write them to the CSV
        for policy in policies:
            writer.writerow({
                'Policy Name': policy['PolicyName'],
                'PolicyId': policy['PolicyId'],
                'Arn': policy['Arn']
            })


##############################################################################

##############################CALL THE fUNCTION#############################



if __name__ == "__main__":
    # Call the list_iam_policies function to retrieve IAM policies
    policies = list_iam_policies()
    
    # Call the write_policies_to_csv function to write policies to a CSV file
    write_policies_to_csv(policies, 'iam_policies.csv')
