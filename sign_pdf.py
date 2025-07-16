import fitz  # PyMuPDF

def assinar_pdf_em_underlines(input_pdf, output_pdf, assinatura_img, pagina_alvo=None):
    doc = fitz.open(input_pdf)
    encontrou = False

    paginas = [doc[pagina_alvo]] if pagina_alvo is not None else doc

    for page in paginas:
        # busca por um campo de assinatura
        resultados = page.search_for("______________")

        if resultados:
            posicao = resultados[2]  # seleção da ocorrência de interesse

            altura_assinatura = 60
            largura_assinatura = posicao.width

            ajuste_centralizacao = 0  # ajuste para centralizar a assinatura na linha
            x0 = posicao.x0 + ajuste_centralizacao
            y0 = posicao.y0

            offset_vertical = 40 # ajuste da posição vertical da assinatura para que a base dela coincida com a linha
            rect = fitz.Rect(x0, y0 - offset_vertical, x0 +
                             largura_assinatura, y0 - offset_vertical + altura_assinatura)

            page.insert_image(rect, filename=assinatura_img)
            encontrou = True
            print(
                f"Assinatura inserida na página {page.number + 1}, posição: {rect}")
            break

    if encontrou:
        doc.save(output_pdf)
        print(f"✅ PDF assinado salvo como: {output_pdf}")
    else:
        if pagina_alvo is not None:
            print(
                f"❌ Nenhum underline encontrado na página {pagina_alvo + 1}.")
        else:
            print("❌ Nenhum underline encontrado no PDF.")

'''
# Exemplo:
assinar_pdf_em_underlines(
    "teste.pdf",
    "teste_assinado.pdf",
    "assinatura.png",
    pagina_alvo=0  # só procura os campos da 1ª página
)
'''
