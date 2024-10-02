source ~/.zshrc
python -m venv venv
source ./venv/bin/activate

echo alias python='./venv/bin/python' >> ./venv/bin/activate
source venv/bin/activate

pip uninstall pandas
pip uninstall matplotlib

pip install pandas
pip install matplotlib
pip install torch torchvision

pip install flake8
alias norminette=flake8

python projection_life.py

deactivate

rm -rf **pycache**
rm -rf venv

<!-- Setting the x-axis scale to logarithmic (set_xscale('log')) in Matplotlib is useful when you have data that spans several orders of magnitude, such as scientific data or financial data.

Logarithmic scaling transforms the data such that each tick mark on the axis represents a power of the base of the logarithm (usually base 10 or base e). This transformation compresses a wide range of values into a more manageable visual range, making it easier to observe variations across different scales.
-->
