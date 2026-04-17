# pipT.sh  (commands + syntax + explanation)

# =========================================================
# 1. INSTALLING PACKAGES WITH pip
# =========================================================

# syntax:
# pip install package_name

pip install requests        # install single package


# =========================================================
# 2. INSTALLING MULTIPLE PACKAGES
# =========================================================

# syntax:
# pip install package1 package2 package3

pip install numpy pandas matplotlib


# =========================================================
# 3. UPGRADING PACKAGES
# =========================================================

# syntax:
# pip install --upgrade package_name

pip install --upgrade requests


# =========================================================
# 4. LISTING INSTALLED PACKAGES
# =========================================================

# syntax:
# pip list

pip list                   # shows all installed packages


# =========================================================
# 5. UNINSTALLING PACKAGES
# =========================================================

# syntax:
# pip uninstall package_name

pip uninstall requests


# =========================================================
# 6. FREEZING INSTALLED PACKAGES
# =========================================================

# syntax:
# pip freeze

pip freeze                # shows exact versions

# save to file
# syntax:
# pip freeze > requirements.txt

pip freeze > requirements.txt


# =========================================================
# 7. USING requirements.txt FILE
# =========================================================

# syntax:
# pip install -r requirements.txt

pip install -r requirements.txt


# =========================================================
# 8. USING VIRTUAL ENVIRONMENTS
# =========================================================

# -------------------------------
# CREATE VIRTUAL ENVIRONMENT
# -------------------------------

# syntax:
# python -m venv env_name

python -m venv myenv


# -------------------------------
# ACTIVATE VIRTUAL ENVIRONMENT
# -------------------------------

# Windows:
myenv\Scripts\activate

# Linux / Mac:
source myenv/bin/activate


# -------------------------------
# DEACTIVATE VIRTUAL ENVIRONMENT
# -------------------------------

# syntax:
deactivate


# -------------------------------
# DELETE VIRTUAL ENVIRONMENT
# -------------------------------

# simply delete folder

# Windows:
rmdir /s myenv

# Linux / Mac:
rm -rf myenv


# =========================================================
# EXTRA NOTES
# =========================================================

# • pip installs packages from PyPI
# • virtual environment keeps dependencies isolated
# • requirements.txt helps reproduce environment
# • always use virtual env in real projects