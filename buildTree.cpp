#include <stdio.h>
#include <iostream>

using namespace std;

FILE *fin;

const int NUM = 5;
const int SIZEofSIG = 8;

int cSig[5][8];
const int lenTree = 4,numTree = 2;




void inputQSig() {
	fin = fopen("cSig.txt", "r");

	for(int i=0; i<NUM; i++)
		for (int j=0; j<SIZEofSIG; j++)
			fscanf(fin,"%d",&cSig[i][j]);

	// scanf("%d",&lenTree);
	// if (SIZEofSIG % lenTree != 0) {
	// 	printf("wrong input\n");
	// 	return;
	// } 
	lenTree = 4;

	numTree = SIZEofSIG / lenTree;
	printf("%d\n",numTree);

	// for(int i=0; i<NUM; i++){
	// 	for (int j=0; j<SIZEofSIG; j++)
	// 		printf("%d ", cSig[i][j]);
	// 	printf("\n");
	// }
}

void insertTree() {

}

int main() {

	inputQSig();
	insertTree();




	return 0;
}
