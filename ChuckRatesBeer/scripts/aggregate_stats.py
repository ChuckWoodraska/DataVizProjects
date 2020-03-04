import pandas
import json


df = pandas.read_json("../data/chuckratesbeer.json")
with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
    # Rating score by count
    print(df['rating_score'].value_counts())
    print(json.dumps(df['rating_score'].value_counts().to_dict()))
    my_dict = df['rating_score'].value_counts().to_dict()
    my_list = []
    e_dict = {}
    for k in my_dict:
        my_list.append([str(k), my_dict[k]])
        my_list.append(["{}_x".format(k), k])
        e_dict[k] = "{}_x".format(k)


    print(json.dumps(e_dict))
    print(json.dumps(my_list))

    # # Find highest
    # print(df.loc[df['rating_score'] == 5.0])
    #
    # # Find lowest rated
    # print(df.loc[df['rating_score'] == 0.5])
    #
    # # Count beer type most
    # print(df['beer_type'].value_counts())
    #
    # # Rating by beer_type
    # print(df.groupby(['beer_type'])['rating_score'].mean())
    # # nf = df.groupby(['beer_type'])
    # # nf.apply()
    #
    # # Make subtypes
    df[["Type", "Subtype"]] = df.beer_type.str.split(" - ", expand=True)
    # # print(df.head())
    # # print(df.groupby(['Type'])['rating_score'].mean())
    # # print(df['Type'].value_counts())
    # # print(df['beer_type'].value_counts())
    # a = df['beer_type'].value_counts()
    # print(a.index)
    # for index, i in enumerate(a.index):
    #     print('{} <span style="float: right; margin-right: 350px;">{}</span><br />'.format(i, a[index]))
    # a = df['Type'].value_counts()
    # print(a.index)
    # for index, i in enumerate(a.index):
    #     print('{} <span style="float: right; margin-right: 350px;">{}</span><br />'.format(i, a[index]))
    # # groudf['beer_type'].value_counts()ped = df.groupby('beer_type').apply(['rating_score'].mean())
    # # print(grouped)
    # # grouped.sort_values('rating_score', ascending=False)
    # # print(grouped)
    df_by_spec_count = df.groupby('beer_type')['rating_score'].agg(['mean', 'count'])
    a = df_by_spec_count.sort_values(by='mean', ascending=False).to_dict()
    for index, i in enumerate(a.index):
        print('{} <span style="float: right; margin-right: 350px;">{}</span><br />'.format(i, a[index]))
    print(df_by_spec_count.sort_values(by='mean', ascending=False))
    #
    df_by_spec_count = df.groupby('Type')['rating_score'].agg(['mean', 'count'])
    print(df_by_spec_count.sort_values(by='mean', ascending=False).to_dict())
    my_dict = df_by_spec_count.to_dict()["count"]
    my_list = []
    for k in my_dict:
        my_list.append([k, my_dict[k]])
    print(my_list)
    e_dict = {}
    my_dict = df_by_spec_count.to_dict()["mean"]
    for k in my_dict:
        my_list.append(["{}_x".format(k), round(my_dict[k], 2)])
        e_dict[k] = "{}_x".format(k)
    print(json.dumps(e_dict))
    print(json.dumps(my_list))

# bid
# abv
# ibu
# beer_name
# beer_type
# brewery_city
# brewery_country
# global_rating_score
# serving_type
# rating_score
