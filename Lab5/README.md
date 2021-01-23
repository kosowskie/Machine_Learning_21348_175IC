```python

```
# Importy
```python
import spacy
import re
from spacy.tokenizer import Tokenizer
from collections import Counter
from spacy import displacy
from spacy.matcher import Matcher
import textacy
```

# Polski moduł
```python
nlp = spacy.load("pl_core_news_sm")
```

#  Utworzenie Doc'a z pliku tekstowego - How to Read a Text File
```python
file_name = 'introduction.txt'
introduction_file_text = open(file_name).read()
introduction_file_doc = nlp(introduction_file_text)
# Extract tokens for the given doc
print ([token.text for token in introduction_file_doc])
```

# Detekcja zdań
```python
about_text=('„Divide et impera!”: dziel, a będziesz rządził; dziel a staniesz się bogaty; dziel a oszukasz ludzi, zaślepisz ich rozum, drwić będziesz ze sprawiedliwości. Sprawiedliwość i władza – słowa nie do pogodzenia.')
about_doc = nlp(about_text)
sentences = list(about_doc.sents)
print(len(sentences))
for sentence in sentences:
    print(sentence)
```

# Przykład, w którym wielokropek (...) jest używany jako separator
```python
def set_custom_boundaries(doc):
    for token in doc[:-1]:
        if token.text == '...' or token.text == 'np.' or token.text == 'm.in.':
            doc[token.i+1].is_sent_start = True
    return doc

ellipsis_text = 'ale też, bez przesady… można z tym żyć, tylko…ja bym tak na przykład…'

custom_nlp = spacy.load("pl_core_news_sm")
custom_nlp.add_pipe(set_custom_boundaries, before='parser')
custom_ellipsis_doc = custom_nlp(ellipsis_text)
custom_ellipsis_sentences = list(custom_ellipsis_doc.sents)
for sentence in custom_ellipsis_sentences:
    print(sentence)
```

```python
ellipsis_doc = nlp(ellipsis_text)
ellipsis_sentences = list(ellipsis_doc.sents)
for sentence in ellipsis_sentences:
   print(sentence)
```
# Tokenizacja za pomocą biblioteki spaCy
## Wypisanie wszystkich tokenów
```python
for token in about_doc:
    print (token, token.idx)
```
## Atrybuty poszczegłonych tokenów
```python
for token in about_doc:
    print (token, token.idx, token.text_with_ws,
    token.is_alpha, token.is_punct, token.is_space,
    token.shape_, token.is_stop)
```
## spaCy umożliwia dostosowanie tokenizacji poprzez aktualizację właściwości tokenizera w obiekcie
```python
custom_nlp = spacy.load('pl_core_news_sm')
prefix_re = spacy.util.compile_prefix_regex(custom_nlp.Defaults.prefixes)
suffix_re = spacy.util.compile_suffix_regex(custom_nlp.Defaults.suffixes)
infix_re = re.compile(r'''[-~]''')

def customize_tokenizer(nlp):
# Adds support to use `-` as the delimiter for tokenization
    return Tokenizer(nlp.vocab, prefix_search=prefix_re.search,
                    suffix_search=suffix_re.search,
                    infix_finditer=infix_re.finditer,
                    token_match=None
                   )


custom_nlp.tokenizer = customize_tokenizer(custom_nlp)
custom_tokenizer_about_doc = custom_nlp(about_text)
print([token.text for token in custom_tokenizer_about_doc])
```
## Słowa pomijane to najpopularniejsze słowa w danym języku. SpaCy udostępnia nam funkcję, dzięki której możemy zastosować takie rozwiązanie
```python
import spacy
spacy_stopwords = spacy.lang.pl.stop_words.STOP_WORDS
len(spacy_stopwords)
for stop_word in list(spacy_stopwords)[:10]:
    print(stop_word)
```
## Można również usunąć słowa pomijane z tekstu wejściowego
```python
for token in about_doc:
    if not token.is_stop:
        print(token)
```
## Można także utworzyć listę tokenów niezawierających słów ignorowanych
```python
about_no_stopword_doc = [token for token in about_doc if not token.is_stop]
print (about_no_stopword_doc)
```
# Lemmatization
```python


conference_help_text = ('Mięso pokroić w kostkę. Cebulę pokroić w kosteczkę i zeszklić na oleju w dużym garnku. Dodać mięso i dokładnie je obsmażyć. '
'Wlać 2 szklanki gorącego bulionu lub wody z solą i pieprzem, zagotować. Następnie dodać połamane suszone grzyby, przykryć, zmniejszyć ogień i gotować przez ok. 45 minut.'
'Dodać listek laurowy, ziela angielskie, kminek, majeranek, powidła śliwkowe lub posiekane śliwki, obrane i pokrojone w kosteczkę obrane jabłko i wymieszać.'
'Dodać odciśniętą kiszoną kapustę oraz wlać szklankę wody, wymieszać. Przykryć i gotować przez ok. 15 minut.'
'Kiełbasę obrać ze skóry, pokroić w kostkę i podsmażyć na patelni. Dodać do kapusty i gotować przez ok. 30 minut. Pod koniec dodać koncentrat pomidorowy.')
conference_help_doc = nlp(conference_help_text)
for token in conference_help_doc:
    print (token, token.lemma_)
```
# Częstotliwość słów - 5 powszechnie występujących słów wraz z ich częstotliwościami
```python
complete_text = 'Mięso pokroić w kostkę. Cebulę pokroić w kosteczkę i zeszklić na oleju w dużym garnku. Dodać mięso i dokładnie je obsmażyć. ' \
                'Wlać 2 szklanki gorącego bulionu lub wody z solą i pieprzem, zagotować. Następnie dodać połamane suszone grzyby, przykryć, zmniejszyć ogień i gotować przez ok. 45 minut.'\
                'Dodać listek laurowy, ziela angielskie, kminek, majeranek, powidła śliwkowe lub posiekane śliwki, obrane i pokrojone w kosteczkę obrane jabłko i wymieszać.'\
                'Dodać odciśniętą kiszoną kapustę oraz wlać szklankę wody, wymieszać. Przykryć i gotować przez ok. 15 minut.'\
                'Kiełbasę obrać ze skóry, pokroić w kostkę i podsmażyć na patelni. Dodać do kapusty i gotować przez ok. 30 minut. Pod koniec dodać koncentrat pomidorowy.'
complete_doc = nlp(complete_text)

words = [token.text for token in complete_doc
          if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
common_words = word_freq.most_common(5)
print (common_words)
```
# Porównanie z Word Frequency i StopWords ten sam tekst ze słowami pomijanymi
```python
words_all = [token.text for token in complete_doc if not token.is_punct]
word_freq_all = Counter(words_all)
common_words_all = word_freq_all.most_common(5)
print (common_words_all)
```
# Część znakowania mowy - w spaCy tagi POS są dostępne jako atrybut w obiekcie Token
```python
for token in about_doc:
    print (token, token.tag_, token.pos_, spacy.explain(token.tag_))
```
# Za pomocą tagów POS można wyodrębnić określoną kategorię słów
```python
nouns = []
adjectives = []
for token in about_doc:
     if token.pos_ == 'NOUN':
         nouns.append(token)
     if token.pos_ == 'ADJ':
         adjectives.append(token)

nouns
```
```python
adjectives
```
# Wizualizacja: przy użyciu displaCy
```python
about_interest_text = ('bulion – mocny rosół, odtłuszczony i podawany na ciepło lub zimno;'
     'bulion – wywar z kości, mięsa, warzyw, służący do gotowania lub duszenia potraw, zup, sosów;.'
     'bulion – koncentrat mięsny lub warzywny, do rozpuszczenia w wodzie.')
about_interest_doc = nlp(about_interest_text)
displacy.render(about_interest_doc, style='dep', jupyter=True)
```
# Funkcje przetwarzania wstępnego
```python
def is_token_allowed(token):
     if (not token or not token.string.strip() or
         token.is_stop or token.is_punct):
         return False
     return True

def preprocess_token(token):

     return token.lemma_.strip().lower()

complete_filtered_tokens = [preprocess_token(token)
    for token in complete_doc if is_token_allowed(token)]
complete_filtered_tokens
```
# Dopasowywanie oparte na regułach za pomocą spaCy
## Dzięki dopasowaniu opartemu na regułach można wyodrębnić imię i nazwisko, które zawsze są rzeczownikami własnymi
```python
matcher = Matcher(nlp.vocab)
text_surname = 'Mam na imię Adam Smith i mieszkam w Gdyni'
nlp_nazwisko = nlp(text_surname)
def extract_full_name(nlp_doc):
     pattern = [{'POS': 'PROPN'}, {'POS': 'PROPN'}]
     matcher.add('FULL_NAME', None, pattern)
     matches = matcher(nlp_doc)
     for match_id, start, end in matches:
         span = nlp_nazwisko[start:end]
         return span.text

extract_full_name(nlp_nazwisko)
```
## Można także użyć dopasowania opartego na regułach, aby wyodrębnić numery telefonów
```python
matcher = Matcher(nlp.vocab)
conference_org_text = ('Mój aktualny'
    'nr telefonu to'
    'dom: 694202137'
    'stacjonarny: (123) 456-789')
def extract_phone_number(nlp_doc):
    pattern = [{'ORTH': '('}, {'SHAPE': 'ddd'},
               {'ORTH': ')'}, {'SHAPE': 'ddd'},
               {'ORTH': '-', 'OP': '?'},
               {'SHAPE': 'ddd'}]
    matcher.add('PHONE_NUMBER', None, pattern)
    matches = matcher(nlp_doc)
    for match_id, start, end in matches:
        span = nlp_doc[start:end]
        return span.text
conference_org_doc = nlp(conference_org_text)
extract_phone_number(conference_org_doc)
```
# Dependency Parsing Using spaCy
```python
ext = 'Emanuel jest dzikiem SW'
doc = nlp(text)
for token in doc:
   print (token.text, token.tag_, token.head.text, token.dep_)
```
# Istnieje szczegółowa lista powiązań wraz z opisami. Można użyć displaCy do wizualizacji drzewa zależności
```python
displacy.serve(doc, style='dep')
```
# Poruszanie się po drzewie i poddrzewie
## spaCy zapewnia atrybuty, takie jak dzieci, lewe, prawa i poddrzewo do nawigacji po drzewie analizy
```python
one_line_about_text = ('Emanuel Kosowski jest dzikiem SW'
   'Holduje kozak backlevery w fullu')
one_line_about_doc = nlp(one_line_about_text)
print([token.text for token in one_line_about_doc[5].children])
print (one_line_about_doc[5].nbor(-1))
print (one_line_about_doc[5].nbor())
print([token.text for token in one_line_about_doc[5].lefts])
print([token.text for token in one_line_about_doc[5].rights])
print (list(one_line_about_doc[5].subtree))
```
## Można skonstruować funkcję, która przyjmuje poddrzewo jako argument i zwraca ciąg, łącząc zawarte w nim słowa
```python
def flatten_tree(tree):
   return ''.join([token.text_with_ws for token in list(tree)]).strip()
print (flatten_tree(one_line_about_doc[5].subtree))
```
# Shallow Parsing
## spaCy ma właściwość noun_chunks w obiekcie Doc. Możesz go użyć do wyodrębnienia fraz rzeczownikowych
```python
conference_text = ('Nadchodzą targi Gamedev wraz GameJam'
    'Odbywać się będą na HSW w Gdyni, 19 maja 2021')
conference_doc = nlp(conference_text)
for chunk in conference_doc.noun_chunks:
    print (chunk)
```
## Wykrywanie fraz czasownika
```python
about_talk_text = ('Ten tekst pokaże zastosowanie'
                   'zastosowanie Natural Language Processing w'
                   'w textacy')
pattern = r'(<VERB>?<ADV>*<VERB>+)'
about_talk_doc = textacy.make_spacy_doc(about_talk_text,
                                        lang='pl_core_news_sm')
verb_phrases = textacy.extract.pos_regex_matches(about_talk_doc, pattern)
for chunk in verb_phrases:
    print(chunk.text)
```

```python
for chunk in about_talk_doc.noun_chunks:
    print (chunk)
```
# Rozpoznawanie nazwanych jednostek
## spaCy ma właściwość ents na obiektach Doc. Można go użyć do wyodrębnienia nazwanych jednostek
```python
class_text = ('Mięso pokroić w kostkę. Cebulę pokroić w kosteczkę i zeszklić na oleju w dużym garnku. Dodać mięso i dokładnie je obsmażyć. ' 
                'Wlać 2 szklanki gorącego bulionu lub wody z solą i pieprzem, zagotować. Następnie dodać połamane suszone grzyby, przykryć, zmniejszyć ogień i gotować przez ok. 45 minut.'
                'Dodać listek laurowy, ziela angielskie, kminek, majeranek, powidła śliwkowe lub posiekane śliwki, obrane i pokrojone w kosteczkę obrane jabłko i wymieszać.')
class_doc = nlp(class_text)
for ent in class_doc.ents:
    print(ent.text, ent.start_char, ent.end_char,
         ent.label_, spacy.explain(ent.label_))

displacy.serve(class_doc, style='ent')
```
