def acronym(x: str):
    """
    given x the name$acronym of a political party, return the acronym
    """
    
    return x.split("$")[1].strip().upper()
    
    
def proper(x: str):
    """
    
    strips city name x from all leading and trailing whitespace and properly capitalizes first word
    if city has two accepted names, uses first accepted form
    """
    
    first_form = x.split("/")[0].strip()
    
    return f"{' '.join([term.capitalize() for term in first_form.split(' ')])}"


def compute_popular(df):
    """
    given dataframe of electoral results from ministerio del interior, compute most popular party and votes by town
    assumes data does not have nulls
    """
    parties_votes = df.drop(columns=df.columns[:13])
    
    df["Popular"] = parties_votes.idxmax(axis=1)
    df["Popular votos"] = parties_votes.max(axis=1)
    
    return df
    