from pyspark.sql import SparkSession
from .models import FileModel
from pyspark.sql.types import * 

class SparkApp:
    def __init__(self,myfile):
        self.spark=SparkSession.builder.appName('cleaner').getOrCreate()
        self.myFile=myfile
        self.sparkContext=self.spark.sparkContext
        self.dataFile=self.spark.read.option('header','true').option('inferschema','true').csv(self.myFile)


    def cleanAll(self):
        dataFile=self.dataFile
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
    
    def recommendSchema(self):
        dataFile=self.dataFile
        result=dataFile.na.drop(how='any')
        clean=result.collect()
        elements=[]
        for ele in clean[1]:
            elements.append(ele)
        print(elements)    
        fields = []
        for x in elements:
            if isinstance(x,int):
                field = StructField(str(x), IntegerType(), nullable=True)
            elif isinstance(x,str):
                field = StructField(str(x), StringType(), nullable=True)
            elif isinstance(x,float):
                field = StructField(str(x), FloatType(), nullable=True)
            elif x in ['False','True']:
                field = StructField(str('BooleanField'), BooleanType(), nullable=True)      
            else:
                print(f"{x} - cannot recognize this")

            fields.append(field)
        return fields




    def cleanThresh(self):
        return 'working'

    def cleanSubset(self):
        ...

