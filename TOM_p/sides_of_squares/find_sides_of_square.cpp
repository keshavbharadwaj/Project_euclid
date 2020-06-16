#include <stdio.h>
using namespace std;

int main()
{
	int x,y,z,w,a,b,c,d,u,o=0;
	int i=0;
	int s1,s2,s3,s4=0;
	for(i=0;i<100;i++)
	{
		x=i;
		y=x+9;
		z=y+x;
		w=z+x;
		
		a=y+9;
		b=a+9;
		c=a+b;
		
		d=w-(b-x+9);
		
		u=w+d;
		o=u+d;
		
		s1=o+u;
		s2=c+a+y+z;
		s3=o+c;
		s4=u+w+z;
		
		if(s1==s2 && s3==s4)
		{
			printf("->->->FOUND: %d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n",x,y,z,w,a,b,c,d,u,o);
			printf("->->->FOUND: %d,%d,%d,%d\n",s1,s2,s3,s4);
			printf("->->->FOUND: \n");
		}
		
		else
		{
			printf("%d,%d,%d,%d,%d,%d,%d,%d,%d,%d\n",x,y,z,w,a,b,c,d,u,o);
			printf("%d,%d,%d,%d\n",s1,s2,s3,s4);
			printf("not found\n");
		}
	}
	return 0;
}
