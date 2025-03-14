from fpdf import FPDF

# Criando o PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

# Adicionando conteúdo ao PDF
conteudo = """Resumo de Artigos Científicos para Teste:

1. Título: Desenvolvimento de Modelos de Machine Learning
Resumo: Este artigo aborda as etapas principais para criar modelos eficientes de aprendizado de máquina, desde a coleta de dados até a validação. O estudo foca na importância de dados balanceados para garantir previsões robustas.

2. Título: Uso de Redes Neurais em Processamento de Linguagem Natural
Resumo: O artigo explora como as redes neurais, incluindo Transformers, revolucionaram o campo de PLN. Estudos indicam que esses modelos superam abordagens tradicionais, especialmente em tarefas de tradução e geração de texto.

3. Título: Avaliação de Algoritmos de Busca Vetorial
Resumo: Este artigo analisa a eficácia de algoritmos de busca vetorial para recuperação de informações em grandes conjuntos de dados. Resultados mostram que técnicas baseadas em embeddings garantem maior precisão.
"""
pdf.multi_cell(0, 10, conteudo)

# Salvando o PDF
pdf.output("artigos_teste.pdf")
print("PDF criado com sucesso!")
