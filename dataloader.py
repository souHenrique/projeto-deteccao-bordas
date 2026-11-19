import os
import glob
import cv2
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt


def carregar_dados_bsds(id_imagem):
    dir_base = os.path.join("archive")

    img_path = os.path.join(dir_base, "images", "train", f"{id_imagem}.jpg")
    mat_path = os.path.join(dir_base, "ground_truth", "train", f"{id_imagem}.mat")

    print(f"-> Procurando imagem em: {img_path}")
    print(f"-> Procurando matriz em: {mat_path}")

    if not os.path.exists(img_path):
        raise FileNotFoundError(f"A IMAGEM não foi encontrada no caminho: {img_path}")

    if not os.path.exists(mat_path):
        raise FileNotFoundError(f"O ARQUIVO .MAT não foi encontrado no caminho: {mat_path}")

    imagem = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    mat = sio.loadmat(mat_path)
    borda_gt = mat["groundTruth"][0, 0]["Boundaries"][0, 0]
    borda_gt_img = (borda_gt * 255).astype(np.uint8)

    return imagem, borda_gt_img


def mostrar_dados(dados_treino):
    indice = 0
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    id_inicial, img_inicial, gt_inicial = dados_treino[indice]
    imagem_artist = ax1.imshow(img_inicial, cmap="gray")
    gt_artist = ax2.imshow(gt_inicial, cmap="gray")

    ax1.set_title(f"Imagem Original ({id_inicial})")
    ax2.set_title("Ground Truth (Bordas Reais)")
    fig.suptitle(f"Imagem {indice + 1}/{len(dados_treino)} - use as setas esquerda/direita")

    def navegar(event):
        nonlocal indice
        if event.key == "right":
            indice = (indice + 1) % len(dados_treino)
        elif event.key == "left":
            indice = (indice - 1) % len(dados_treino)
        else:
            return

        id_imagem, imagem, gt = dados_treino[indice]
        imagem_artist.set_data(imagem)
        gt_artist.set_data(gt)
        ax1.set_title(f"Imagem Original ({id_imagem})")
        ax2.set_title("Ground Truth (Bordas Reais)")
        fig.suptitle(
            f"Imagem {indice + 1}/{len(dados_treino)} - use as setas esquerda/direita"
        )
        fig.canvas.draw_idle()

    fig.canvas.mpl_connect("key_press_event", navegar)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    pasta_imagens = os.path.join("archive", "images", "train")
    imagens_disponiveis = sorted(glob.glob(os.path.join(pasta_imagens, "*.jpg")))

    if not imagens_disponiveis:
        print(f"Não há nenhuma imagem na pasta: {pasta_imagens}")
    else:
        dados_treino = []
        for img_path in imagens_disponiveis:
            id_imagem = os.path.splitext(os.path.basename(img_path))[0]
            imagem, gt = carregar_dados_bsds(id_imagem)
            dados_treino.append((id_imagem, imagem, gt))

        print(f"Foram carregados {len(dados_treino)} pares de imagem e ground truth.")
        mostrar_dados(dados_treino)