import yfinance as yf 
import pandas as pd

start = "2022-01-01"
end= "2022-12-16"
tickers = 'KDSI.JK FMII.JK LPGI.JK ARGO.JK PRAS.JK CITA.JK PUDP.JK UNIC.JK INDR.JK AISA.JK PNBN.JK ASDM.JK BABP.JK EXCL.JK BKDP.JK SHID.JK JSMR.JK SPMA.JK AIMS.JK PSKT.JK VOKS.JK ABDA.JK TFCO.JK ASGR.JK SULI.JK TRST.JK FPNI.JK SQMI.JK LMPI.JK '

df = yf.download(tickers,
                   start=start,
                   end=end)
df.index = df.index.strftime('%Y-%m-%d')
df.to_excel('IHSG.xlsx')