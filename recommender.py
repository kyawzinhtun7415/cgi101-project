import pandas as pd

def top_k_items(similarity_csv,item_name,k):
    try:
        similarity_df = pd.read_csv(similarity_csv,index_col=0)
    except FileNotFoundError:
        print("similarity csv file missing")
        return(1)

    return similarity_df.loc[item_name].sort_values(ascending=False).head(k+1).index[1:].to_list()


def main():
    print(top_k_items("drinks_similarity.csv",'仙草凍奶茶',5))

    print(top_k_items("drinks_similarity_toppings.csv",'仙草凍奶茶+珍珠',5))

if __name__=='__main__':
    main()