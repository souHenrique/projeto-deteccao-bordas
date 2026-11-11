import os
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
    
    borda_gt = mat['groundTruth'][0, 0]['Boundaries'][0, 0]
    
    borda_gt_img = (borda_gt * 255).astype(np.uint8)
    
    return imagem, borda_gt_img

if __name__ == "__main__":
    import glob
        
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

        print(f"Foram carregadas {len(dados_treino)} pares de imagem e ground truth.")

        id_imagem, img, gt = dados_treino[0]
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        ax1.imshow(img, cmap='gray')
        ax1.set_title(f"Imagem Original ({id_imagem})")
        ax2.imshow(gt, cmap='gray')
        ax2.set_title("Ground Truth (Bordas Reais)")
        plt.show()