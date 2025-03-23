# MICA - Ferramenta de Gerenciamento de Projetos com IA

Este projeto implementa uma ferramenta Streamlit que utiliza o modelo de Inteligência Artificial Gemini para auxiliar na criação de planos de gerenciamento de projetos, baseados na metodologia MICA (METHODOLOGY IDENTIFICATION AND CHOICE ANALYSIS).

## Funcionalidades

* **Análise MICA:** Permite aos usuários inserir informações sobre o projeto (criticidade, equipe, tamanho, cultura organizacional, dinamismo) e o tempo de conclusão desejado.
* **Geração de Plano de Gerenciamento:** Utiliza o modelo Gemini para gerar um plano de gerenciamento personalizado, considerando os fatores MICA e o tempo de conclusão.
* **Visualização de Resultados:** Exibe o plano de gerenciamento gerado em uma interface Streamlit amigável.
* **Salvar e Gerenciar Planos:** Permite salvar os planos gerados e visualizar o progresso das fases do projeto.

## Pré-requisitos

* Python 3.x
* Bibliotecas Python:
    * streamlit
    * nltk
    * pandas
    * google-generativeai
    * logging
    * base64
    * re
* Uma chave de API válida para o Google Gemini.
* Arquivo `Logo.png` no mesmo diretório do script ou em um caminho especificado.
* Arquivo `function.py` contendo as funções `obter_valor_criticidade`, `obter_valor_equipe`, `obter_valor_dinamismo`, `obter_valor_cultura` e `obter_valor_tamanho`.

## Instalação

1.  Clone o repositório:

    ```bash
    git clone [https://github.com/dolthub/dolt](https://github.com/dolthub/dolt)
    ```

2.  Instale as dependências:

    ```bash
    pip install streamlit nltk pandas google-generativeai
    ```

3.  Baixe os recursos NLTK necessários:

    ```python
    import nltk
    nltk.download('punkt')
    ```

4.  Configure a chave de API do Google Gemini na variável `PI_KEY` no script.
5.  Certifique-se de que os arquivos `Logo.png` e `function.py` estejam no mesmo diretório do script.

## Uso

1.  Execute o script Streamlit:

    ```bash
    streamlit run seu_script.py
    ```

2.  Acesse o aplicativo Streamlit no seu navegador.
3.  Na aba "Criar plano de gerenciamento", preencha as informações do projeto e o tempo de conclusão desejado.
4.  Clique em "ENVIAR" para gerar o plano de gerenciamento.
5.  O plano gerado será exibido na tela.
6.  Insira um título e clique em "Salvar" para salvar o plano.
7.  Na aba "Galeria", visualize os planos salvos e acompanhe o progresso das fases do projeto.

## Estrutura do Código

* **`main()`:** Função principal que define a interface Streamlit e a lógica do aplicativo.
* **`img_to_base64(image_path)`:** Função para converter uma imagem em Base64.
* **`obter_valor_criticidade`, `obter_valor_equipe`, `obter_valor_dinamismo`, `obter_valor_cultura` e `obter_valor_tamanho`:** Funções definidas no arquivo `function.py` para obter os valores correspondentes aos fatores MICA.

## Observações

* Certifique-se de que a chave de API do Google Gemini esteja configurada corretamente.
* A precisão e a qualidade do plano de gerenciamento gerado dependem da qualidade do modelo Gemini e das informações fornecidas pelo usuário.
* O arquivo `function.py` deve conter as funções necessárias para obter os valores dos fatores MICA.
* O arquivo `Logo.png` é usado para exibir o logotipo na barra lateral.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) ou enviar solicitações de pull (pull requests) para melhorar este projeto.
