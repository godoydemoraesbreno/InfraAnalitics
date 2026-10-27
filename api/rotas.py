from fastapi import APIRouter
from utils.script import varredura, obter_alvos, gerar_lista_ativos, insercao_de_dados

# criar o router
router = APIRouter()

#rota que recebe o limite de ip e faz o scan
@router.get("/scan/{limite}")
async def rodar_scan(limite: int):
    if limite > 0 and limite < 255:
        alvos = obter_alvos(limite)
        ips_gerados = gerar_lista_ativos(alvos)

        if len(ips_gerados) > 0:
            insercao_de_dados(ips_gerados)
            return {"status": "Sucesso", "ips_ativos": ips_gerados}
        else:
            return {"status": "Sucesso, mas nenhum ip ativo."}
        
    else:
        return {"status": "Erro, limite ultrapassado"}
