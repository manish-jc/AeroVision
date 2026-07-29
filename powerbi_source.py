import sys

# Add your project folder to Python's path
sys.path.append(r"C:\Users\Manish J C\OneDrive\Documents\Desktop\Aerovision")

from main import run_pipeline

# Power BI imports the dataframe named 'dataset'
dataset = run_pipeline(
    save_json=False,
    save_csv=False,
    verbose=False
)