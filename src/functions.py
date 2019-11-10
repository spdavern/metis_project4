import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.tokenize import punkt

def run():
    print("This file defines functions used to process TED talks...")

def get_sents(df_with_transcript,word,sentences_before=2,sentences_after=None):
    """Function that extracts snippets of sentences.  The snippets will include
    the sentence containing the word and those around it from n 'sentences_before'
    to m 'sentences_after'.  If 'word' occurs multiple times in the transcript
    the multiple snippets, as defined, will be concatinated.
    -----
    inputs:
        df_with_transcript: A pandas dataframe with a column named 'transcript'
            which contain the transcript of the talk to be parsed.
        word: A string containing the word that will be used to find sentences
            containing that word.
        sentences_before: An integer - the number of sentences before the one
            containing 'word' that will be included in the snippet returned.
        sentences_after: An integer - the number of sentences after the one
            containing 'word' that will be included in the snippet returned.
    returns:
        A copy of the input pandas dataframe containing two new columns:
            df.word: string - the collection of snippets from the transcript
            df.n_word_sents: integer - the number of sentences in the transcript
              which contain at least 1 occurrence of the word.
    """
    sentences_after = sentences_before if sentences_after is None else sentences_after
    output=df_with_transcript.copy()
    for i, row in df_with_transcript.iterrows():
        talk = df_with_transcript.loc[i].transcript
        sentences = pd.DataFrame(sent_tokenize(talk))
        sentences_with_word = sentences[sentences[0].str.contains(word,case=False)]
        output.loc[i,'n_'+word+'_sents'] = len(sentences_with_word)
        snippet_with_word = sentences_with_word.copy()
        for j in sentences_with_word.index:
            lower_bound = max(0,j-sentences_before)
            upper_bound = min(j+sentences_after+1,len(sentences))
            snippet_with_word.loc[j,0] = sentences[lower_bound:upper_bound][0].str.cat(sep=' ')
        output.loc[i,word] = snippet_with_word[0].str.cat(sep=' ')
    return output

def display_topics(model, feature_names, num_top_words, topic_names=None):
    """Returns top n=num_top_words words from the doc_topic matrix.
    This function came from the Metis Topic_Modeling_LSA_NMF.ipynb notebook but I added the
    docstring.
    -----
    inputs:
        model: The dimensionality reduced topic model containing an `components_` attribute.
            For example, the fit_transformed lsa object.
        feature_names: a list of strings - typically the result of vectorizer.get_feature_names()
            generally an alphabetical list of word contained in the entire corpus of documents.
        num_top_words: integer - the number of words to return of the top words in the topic model
        topic_names: a list of strings - typically terms that describe the topics
    return:
        provides stdout printing of the top n words from the doc_topic matrix.
    """
    for ix, topic in enumerate(model.components_):
        if not topic_names or not topic_names[ix]:
            print("\nTopic ", ix)
        else:
            print("\nTopic: '",topic_names[ix],"'")
        print(", ".join([feature_names[i]
                        for i in topic.argsort()[:-num_top_words - 1:-1]]))
    return

def unit_norm(df,demean=False):
    """Returns a pandas dataframe with df[0],df[1] divided by sqrt(df[0]^2+df[1]^2)
    ------
    inputs 
        df: a pandas dataframe with columns named 0 and 1
        demean: boolean: if True the mean of columns 0 and 1 are subtracted from each rows values.
    return:
        a copy of the input df with columns 0 and 1 transformed.
    """
    if demean:
        x_mean, y_mean = df.mean()
    else:
        x_mean, y_mean = 0,0
    df2=df.copy()
    for i,row in df.iterrows():
        x, y = row[0].copy()-x_mean, row[1].copy()-y_mean
        df2.iloc[i,0]=x/(x**2+y**2)**0.5
        df2.iloc[i,1]=y/(x**2+y**2)**0.5
    return df2

if __name__ == '__main__':
    run()