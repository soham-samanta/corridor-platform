# Function to extract data from csv file bassed on columns names
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import glob
from sklearn import metrics


def exctocsvtopandas(path):
    # path = r'C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\chakravyuh\\data'
    # extension = 'xlsx'
    # os.chdir(path)
    # result = glob.glob('*.{}'.format(extension))
    # read_file = pd.read_excel(result[0])
  
    # # Write the dataframe object
    # # into csv file
    # read_file.to_csv ("Test.csv", index = None, header=True)

    # read csv file and convert 
    # into a dataframe object
    df = pd.DataFrame(pd.read_csv(path + "\data\Test.csv"))
    return df


def confmat(actual, predicted, threshold, df, path):
    print( "-------------------------")
    print(predicted)
    print(df[predicted])
    df['discrete_pred'] = pd.cut(x=df[predicted], bins=[0, threshold, 1], labels=[0, 1])
    print(df)
    dir_name = path + '\extract\generatedcharts'
    plt.rcParams["savefig.directory"] = os.chdir(os.path.dirname(dir_name))
    confusion_matrix = metrics.confusion_matrix(df[actual], df['discrete_pred'])

    cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels =[False, True])

    cm_display.plot()
    
    plt.savefig('conf_mat.png')
    return None

# def scatterplot(x, y):
#     fig, ax = plt.subplots()
#     ax.scatter(df[x], df[y])
#     dir_name = r'C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platform\chakravyuh\extract\generatedcharts'
#     plt.rcParams["savefig.directory"] = os.chdir(os.path.dirname(dir_name))
#     plt.savefig('scatter.png')

# def hist(x):
#     fig, ax = plt.subplots()

#     ax.hist(df[x], bins=10, linewidth=0.5, edgecolor="white")
#     dir_name = r'C:\Users\KIIT\Prerak\Prerak_Code\CorridorPlatforms\corridor-platformchakravyuh\extract\generatedcharts'
#     plt.rcParams["savefig.directory"] = os.chdir(os.path.dirname(dir_name))
#     plt.savefig('hist.png')

# df =  exctocsvtopandas()
# confmat("model_target", "model_output", 0.8, df)
