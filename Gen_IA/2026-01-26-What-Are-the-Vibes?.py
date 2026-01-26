"""😊 O que são as vibrações? 🙁

Neste exercício final, você construirá uma ferramenta simples para ajudá-lo a decidir se vale a pena assistir a um filme com base em revisões de texto. Ao analisar se as avaliações são positivas ou negativas, você pode ter uma noção de se as pessoas gostaram do filme ou não.

Vamos começar!

    Configure Seu Ambiente

    Inicie um script Python e verifique se as bibliotecas Python necessárias foram instaladas:

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

    Reúna Seus Dados

    Crie uma lista de avaliações de filmes de exemplo, pergunte a alguns amigos ou escolha as principais avaliações on-line. Cada avaliação deve expressar uma opinião positiva ou negativa.

    Rotule Seus Dados

    Rotule cada revisão como "positiva" ou "negativa". Exemplo:

reviews = ['This movie was fantastic! A must-watch.',
           'I didn\'t enjoy this movie at all.',
           'Amazing storyline and great acting!',
           'The plot was dull and predictable.',
           'Loved the cinematography! Highly recommended.']

labels = ['positive', 'negative', 'positive', 'negative', 'positive']

    Vectorize os dados de texto

    Converta seus dados de texto em números que o computador possa entender usando CountVectorizer:

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(reviews)

    Dividir os dados

    Divida seus dados em conjuntos de treinamento e teste para que o computador possa aprender com alguns dados e ser testado no resto:

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

    Treine o Modelo

    Crie um classificador Naive Bayes e treine-o usando os dados de treinamento:

model = MultinomialNB()
model.fit(x_train, y_train)

    Teste o modelo

    Use o modelo treinado para prever as vibrações dos dados do teste:

y_pred = model.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)

print('Accuracy:', accuracy)

    Interpretar os resultados

Por fim, você pode decidir se o filme tem "Boas vibrações!" baseado na precisão do seu modelo. Se a precisão estiver acima de 80%, imprima "Boas vibrações!"

if accuracy > 0.8:
  print('Good vibes. Book the ticket!')
else:
  print('Needs more work!')"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

reviews = [
    "This movie was fantastic! A must-watch.",
    "I didn't enjoy this movie at all.",
    "Amazing storyline and great acting!",
    "The plot was dull and predictable.",
    "Loved the cinematography! Highly recommended.",
]

labels = ["positive", "negative", "positive", "negative", "positive"]

vectorizer = CountVectorizer()

x = vectorizer.fit_transform(reviews)

x_train, x_test, y_train, y_test = train_test_split(
    x, labels, test_size=0.2, random_state=42
)

model = MultinomialNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)

if accuracy > 0.8:
    print("Good vibes. Book the ticket!")
else:
    print("Needs more work!")
