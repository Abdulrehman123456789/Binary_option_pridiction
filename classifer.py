import time
import pyautogui

def takeaction(y):


	#down button cordinates
	dx=848
	dy=560


	#up button cordinates
	ux=1130
	uy=566


	if y==0:
		print("down")
		pyautogui.click(x=dx, y=dy)

	else:
		print("up")
		pyautogui.click(x=ux, y=uy) 




while True:

	f1=open("sync.txt","r")
	syncdata=f1.read()
	f1.close()
	
	if syncdata=="1":

		print(syncdata)



		f=open('tradedata.txt','r')
		data=f.read()
		f.close()
		lines=data.split('\n')


		print(lines)


		linelengtharr=[]

		for i in range(0,len(lines)-1):
			arr=lines[i].split("/")
			l=len(arr)-1
			linelengtharr.append(l)

		print("linelength",linelengtharr)


		smallestlength=min(linelengtharr)

		print("smallestlength",smallestlength)

		temparr=[]
		finalarrx=[]
		for j in range(0,len(lines)-2):
			linearr=lines[j].split("/")
			if len(linearr)>=smallestlength:
				print("linestaken",j+1)
				for k in range(len(linearr)-smallestlength-1,len(linearr)-1):
					temparr.append(linearr[k])

				finalarrx.append(temparr)
				temparr=[]


		print("x values")
		print(finalarrx)



		finalarry=[]
		for j in range(0,len(lines)-2):
			linearr1=lines[j].split("/")
			if len(linearr1)>smallestlength:
				linearr2=lines[j+1].split("/")
				if len(linearr2)<2:
					print("blankline so cheaking next line")
					linearr2=lines[j+2].split("/")
				print("comparing")
				if float(linearr1[-2])<float(linearr2[-2]):
					print(linearr1[-2],linearr2[-2],1)
					finalarry.append(1)
				else:
					finalarry.append(0)
					print(linearr1[-2],linearr2[-2],0)



		print("y value")
		print(finalarry)










		import numpy as np
		trainx=np.array(finalarrx,dtype=float)
		trainy=np.array(finalarry,dtype=float)

		print("train_x")
		print(trainx)
		print("train_y")
		print(trainy)
  




		#training

		from sklearn.neighbors import KNeighborsClassifier
		classifier1 = KNeighborsClassifier(n_neighbors=5)
		classifier1.fit(trainx,trainy)


		from sklearn import svm
		classifier2=svm.SVC()
		classifier2.fit(trainx,trainy)



		from sklearn.naive_bayes import GaussianNB
		classifier3=GaussianNB()
		classifier3.fit(trainx,trainy)


		from sklearn.linear_model import LogisticRegression
		classifier4=LogisticRegression()
		classifier4.fit(trainx,trainy)


		from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
		classifier5=QuadraticDiscriminantAnalysis()
		classifier5.fit(trainx,trainy)





		x_pred=[]
		x_predarr=lines[-2].split("/")
		if len(x_predarr)>smallestlength:
			for k in range(len(x_predarr)-smallestlength-1,len(x_predarr)-1):
				x_pred.append(x_predarr[k])

			x_pred=np.array([x_pred],dtype=float)
			print("test_data")
			print(x_pred)



			#testing

			NUM_OF_1=0
			NUM_OF_0=0

			y_pred = classifier1.predict(x_pred)
			print("pridectes value of K_NEAREST_NEIGHBOURS")
			print(y_pred)
			if y_pred[0]==1:
				NUM_OF_1=NUM_OF_1+1
			else:
				NUM_OF_0=NUM_OF_0+1




			y_pred = classifier2.predict(x_pred)
			print("pridectes value of SVM")
			print(y_pred)
			if y_pred[0]==1:
				NUM_OF_1=NUM_OF_1+1
			else:
				NUM_OF_0=NUM_OF_0+1



			y_pred = classifier3.predict(x_pred)
			print("pridectes value of naive_bayes")
			print(y_pred)
			if y_pred[0]==1:
				NUM_OF_1=NUM_OF_1+1
			else:
				NUM_OF_0=NUM_OF_0+1


			y_pred = classifier4.predict(x_pred)
			print("pridectes value of LogisticRegression")
			print(y_pred)
			if y_pred[0]==1:
				NUM_OF_1=NUM_OF_1+1
			else:
				NUM_OF_0=NUM_OF_0+1


			y_pred = classifier5.predict(x_pred)
			print("pridectes value of QuadraticDiscriminantAnalysis")
			print(y_pred)
			if y_pred[0]==1:
				NUM_OF_1=NUM_OF_1+1
			else:
				NUM_OF_0=NUM_OF_0+1













			prefered_correct_prediction=3

			if NUM_OF_1>=prefered_correct_prediction:
				takeaction(1)
			if NUM_OF_0>=prefered_correct_prediction:
				takeaction(0)


			time.sleep(7)





				

			#takeaction(y_pred)