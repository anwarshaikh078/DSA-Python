import java.util.*;
class arraySort
{
	public static void main(String args[])
	{
		Scanner ob=new Scanner(System.in);
		int []arr=new int[5];
		for(int i=0;i<5;i++)
		{
			arr[i]=ob.nextInt();
		}
		int temp=arr[0];

		for(int i=0;i<5;i++)
		{
			if(temp>arr[i])
			{
				temp2=temp;
				temp=arr[i];
				arr[i]=temp2;
			}	
			
		}
		for(int i=0;i<5;i++)
		{
			System.out.println(""+arr[i]);
		}	
	}
}
