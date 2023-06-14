from pyspark.sql import SparkSession

class SparkApp:
    def __init__(self,myfile):
        self.spark=SparkSession.builder.appName('cleaner').getOrCreate()
        self.myFile=myfile
        self.sparkContext=self.spark.sparkContext

    def cleanAll(self):
        dataFile=self.spark.read.option('header','true').option('inferschema','true').csv(self.myFile)
        result=dataFile.na.drop(how='all')
        # Convert the DataFrame to a Pandas DataFrame
        pandas_df = result.toPandas()
        # Convert the Pandas DataFrame to HTML
        html_table = pandas_df.to_html()
        return html_table
    
    def cleanAny(self):
        myData=self.spark.read.option('header','true').option('inferschema','true').csv(self.myFile)
        result=myData.na.drop(how='any')
        # Convert the DataFrame to a Pandas DataFrame
        pandas_df = result.toPandas()
        # Convert the Pandas DataFrame to HTML
        html_table = pandas_df.to_html()
        return html_table

    def cleanThresh(self):
        return 'working'

    def cleanSubset(self):
        ...

