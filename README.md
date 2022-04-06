[![Python Validator](https://github.com/CS-AE/terraform-setup/actions/workflows/validator.yml/badge.svg)](https://github.com/CS-AE/terraform-setup/actions/workflows/validator.yml)

# Terraform Setup

Simplete script to create a terraform project from standard

## Description

Simple script to create a tgerraform project from a standard template ,Created this because I really couldent be bothered creating the same files each time a new project was started. 

## Getting Started

### Dependencies

* Script has a dependancy on `ruamel.yaml` libraries

### Installing

* Adding dependancies:
`pip3 install ruamel.yaml`

* Clone repo to wherever you like

* Create symlink in one of your path files, doesnt really matter where and point it to terraform-setup python script `ln -s /your/cloned/directory/terraform-setup/terraform-setup /bin/terraform-setup`

### Executing program

Run the terraform setup command below and it'll ask for your project name , Job done

```terraform-setup```

## Help

None really, simple script , feel free to raise a pull request if you want anything changing, dont really have time to activly maintain this other than merging PRs. 

## Version History

* 1.0
    * Initial Release
