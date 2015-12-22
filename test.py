tc = input("Enter no of test cases: ")
for T in range(0,int(tc)):
  weightTokens = input().split(' ')
  W = int(weightTokens[1]) - int(weightTokens[0])
  if W <= 0:
    print("This is impossible.")
    continue

  N = int(input())
  di =[0] * N
  wi =[0] * N
  Cost = [0] * (W+1)
  
  for i in range(0,N):
    tokens = input().split(' ')
    di[i] = int(tokens[0])
    wi[i] = int(tokens[1])
    
  Cost[0] = 0

  for i in range(1,W+1):
    Cost[i] = 10000 * 510
    for k in range(0,N):
      if i >= wi[k] :
        if Cost[i] > (Cost[i - wi[k]] + di[k]) :
          Cost[i] = Cost[i - wi[k]] + di[k]

  if (Cost[W] == 10000 * 510):
    print("This is impossible.")
  else :
    print("The minimum amount of money in the piggy-bank is %d." %(Cost[W]))
