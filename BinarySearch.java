import java.util.*;
import java.*;
class BinarySearch
{
	public static int bin(int []arr,int ele,int lower,int upper)
	{

		int mid=( upper + lower )/2;
		if(upper < lower)
		{
			return -1;
		}
		else
		{
			if(arr[mid] > ele)
			{		
				return bin(arr,ele,lower,mid-1);
			}
			else if(arr[mid] < ele)
			{
				return bin(arr,ele,mid+1,upper);	
			}
			else
			{
				return mid;
			}		
		}
			
	}
	public static void main(String []args)
	{
		Scanner ob=new Scanner(System.in);
		System.out.println("Enter 10 elements in Array:");
		int []arr=new int[10];
		for(int i=0;i<10;i++)
		{
			arr[i]=ob.nextInt();
		}
		System.out.println("Enter element to find");
		int element=ob.nextInt();
		int found=bin(arr,element,0,9);
		System.out.println("Found at position:"+found);
	}
}