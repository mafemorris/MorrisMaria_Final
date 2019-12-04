#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;


template <class T>
void escribe(string archivo, T* datos, int n_dat){
  ofstream outfile;
  //abre el archivo.
  outfile.open(archivo);

  for (int i=0; i < n_dat; i++){
    outfile << datos[i] << endl;
  }
  //cierra el archivo.
  outfile.close(); 
}

void parciales(float** u, float deltax, float deltat, int pasosx, int pasost, float xmin);

int main(){
    float xmin = 0;
    float xmax = 2;
    float tmin = 0;
    float tmax = 0.5;
    float deltat = 0.01;
    float deltax = 0.01;

    int pasosx = (xmax-xmin)/deltax;
    int pasost = (tmax-tmin)/deltat;

    float** u = new float*[pasost];

    parciales(u,deltax,deltat,pasosx,pasost, xmin);

    escribe("solucion.txt", u[pasost-2], pasosx);
    escribe("condicion.txt", u[0], pasosx);

    delete* u;
    return 0;
}

float inicondicion(float x){
    return exp(-pow((x-1)/0.25,2)*0.5);
}

void parciales(float** u, float deltax, float deltat, int pasosx, int pasost, float xmin){
    float x = xmin;
    for(int n = 0; n< pasost; n++){
        u[n] = new float[pasosx];
        for(int j = 0; j< pasosx; j++){
            if(n==0){
                u[n][j] = inicondicion(x);
                x += deltax;
            }
            else if(j==pasosx-1){
                u[n][j] = 0;
            }
            else{
                u[n][j] = u[n-1][j]*(1-(deltat/deltax)*(u[n-1][j+1] - u[n-1][j]));
            }
        }
    }
}