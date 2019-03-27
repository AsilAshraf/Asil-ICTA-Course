var num=263;
var rev=0;
var rem=0;
var x=reverse(num,rev,rem);
console.log(rev);
function reverse(a,b,c)
{
while(num>0)
{
    rem=num%10;
rev=rev*10+rem;
num=parseInt(num/10);

}
return rev;
}
