from flask import Flask
import pandas as pd

server = Flask(__name__)

@server.route("/")
def etl_sub():
    output_str = ""
    medals_url = "http://winterolympicsmedals.com/medals.csv"
    if medals_url != "http://winterolympicsmedals.com/medals.csv":
        print("Unable to connect to appropriate URL. Retry using 'http://winterolympicsmedals.com/medals.csv'")
    #fetch a file from an URL
    df = pd.read_csv(medals_url)
    print('The original medals data has', len(df), 'rows', 'and', len(df.columns), 'columns')
    print('The first 10 rows of the original dataset:')
    print(df.head(10))
    #print(df)
    #print("Original Columns:" + list(df.columns))
    # removed the "Discipline" column
    del df['Discipline']
    del df['Event']
    #print("Modified Columns:" + list(df.columns))
    
    print('The modified medals data has', len(df), 'rows', 'and', len(df.columns), 'columns')

    print("The first 10 rows of the modified dataset:")
    print(df.head(10))

    #find medals won by USA and CANADA
    usa_medals = df[df["NOC"] == "USA"]
    #usa_medals.head()
    canada_medals = df[df["NOC"] == "CAN"]
    
    print("Information about US and Canada medals:")
    total_us_medals = usa_medals.shape[0]
    print('USA won ', total_us_medals, ' Winter Olympic medals since 1924')
    total_canada_medals = canada_medals.shape[0]
    print('Canada won ', total_canada_medals, ' Winter Olympic medals since 1924')

    # find all US Medals won in 2006
    year = 2006
    usa_medals_year = usa_medals[usa_medals["Year"] == year]

    usa_medal_count_year = usa_medals_year.shape[0]

    print('USA won', usa_medal_count_year, 'medals in', year, 'Winter Olympics')
    output_str = output_str + ' USA won ' + str(usa_medal_count_year) + ' medals in ' + str(year) + ' Winter Olympics '
    print("Converted to a JSON file named usa_2006.json:")
    # convert the data to JSON and write to a file
    json_year = usa_medals_year.to_json(orient = 'records')
    print(json_year)

    with open("usa_2006.json", "w") as outfile:
        outfile.write(json_year)
    
    return output_str
        
if __name__ == "__main__":
    server.run(host='0.0.0.0')