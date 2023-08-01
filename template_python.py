#Templating using pyhton
# xml and yaml parsing

from string import Template

#string template
sample_template = Template("THIS IS $name")
final_document = sample_template.substitute({'name':'SHIVAM'})
print(final_document)

# file template
with open("terafform_main.template" ,"r") as aws_template:
    file_data = aws_template.read()
    template_data = Template(file_data)
    str_data = template_data.substitute({"providername":"aws",
                            "region":"us-east-1",
                            "key":"123564"})
    with open("main.tf","w+") as main_file:
        main_file.write(str_data)