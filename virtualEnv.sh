# It is: A mini empty Python installation just for your project

python -m venv .venv #create virtual environment
# | Part   | Meaning               |
# | ------ | --------------------- |
# | python | run Python            |
# | -m     | run module            |
# | venv   | module to create venv |
# | .venv  | folder name           |

.venv\Scripts\Activate.ps1 #activate virtal environment using powershell

Get-Command python #Check if Virtual Environment is Active using powershell

deactivate #Deactivate Virtual Environment

#if you go to other project, deactive your current environment, activate that environment



