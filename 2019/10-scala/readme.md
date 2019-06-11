##5
var listaQuantidade = List()
for( (name, quantidade) <- quantity_ingredients){
    listaQuantidade = listaQuantidade ::: List(quantidade)
}
println( s"Média: " + mean(listaQuantidade))
println( s"Désvio padrão: " + stdDev(listaQuantidade))
