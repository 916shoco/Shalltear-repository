@bot.command(name="calcular")
async def calculate_expression(ctx, *expression):
    expression = "".join(expression)

    print(expression)
  
    response = eval(expression)
    
    await ctx.send("A resposta é: " + str(response))