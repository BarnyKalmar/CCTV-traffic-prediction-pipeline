from pyspark.ml.feature import VectorAssembler
from pyspark.sql import SparkSession
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator


def deploy_schema(csv_path):

    #initiate session
    spark = (
        SparkSession.builder
            .master("local[*]")
            .appName("RandomForestCarRegressor")
            .getOrCreate()
    )


    df = spark.read.csv(csv_path, header=True, inferSchema=True)

    #assemble vecors from csv for learning

    vec_assembler = VectorAssembler(
        inputCols=['month','day','time_of_day','is_weekday'],
                  outputCol = 'features')
    vector_df = vec_assembler.transform(df)


    train_set,test_set = vector_df.randomSplit([8.0,2.0], 42)


    rf = RandomForestRegressor(numTrees=100, maxDepth=30, featuresCol='features', labelCol='car_count')
    model = rf.fit(train_set)
    predictions = model.transform(test_set)

    evaluator1 = RegressionEvaluator(labelCol='car_count', predictionCol='prediction', metricName='rmse')
    rmse = evaluator1.evaluate(predictions)
    evaluator2 = RegressionEvaluator(labelCol='car_count', predictionCol='prediction',metricName='mae')
    mae = evaluator2.evaluate(predictions)
    evaluator3 = RegressionEvaluator(labelCol='car_count', predictionCol='prediction',metricName='r2')
    r2 = evaluator3.evaluate(predictions)

    print(rmse, mae, r2)

    spark.stop()

