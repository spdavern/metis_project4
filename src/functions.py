import pandas as pd
from nltk.tokenize import sent_tokenize
from nltk.tokenize import punkt

def run():
    print("Defining functions to process talks...")

def get_sents(df_with_transcript,word,sentences_before=2,sentences_after=None):
    """
    Function that extracts a snippet of sentences.  The snippet will include
    the sentence containing the word and those around it from n 'sentences_before'
    to m 'sentences_after'.  If 'word' occurs multiple times in the transcript
    the multiple snippets, as defined, will be concatinated.
    -----
    inputs:
        df_with_transcript: A pandas dataframe with a column named 'transcript'
            contain the transcript of the talk to be parsed.
        word: A string containing the word that will be used to find sentences
            containing that word.
        sentences_before: An integer - the number of sentences before the one
            containing 'word' that will be included in the snippet returned.
        sentences_after: An integer - the number of sentences after the one
            containing 'word' that will be included in the snippet returned.
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
            upper_bound = min(j+sentences_after,len(sentences))
            snippet_with_word.loc[j,0] = sentences[lower_bound:upper_bound][0].str.cat(sep=' ')
        output.loc[i,word] = snippet_with_word[0].str.cat(sep=' ')
    return output
    
if __name__ == '__main__':
    run()