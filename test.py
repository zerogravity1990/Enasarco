import sys
import main



agente = main.Agent(sys.argv[1],sys.argv[2])
fattura = main.Invoice(sys.argv[3], sys.argv[4], sys.argv[5])
print agente.name, agente.mandate
print fattura.date, fattura.number, fattura.net_value
par = main.Parameters()
par.loader(par.config_file_path)
calcolatore = main.Algorithms()
calcolatore.calc_enasarco(fattura.net_value, par.rate)

print calcolatore.result
