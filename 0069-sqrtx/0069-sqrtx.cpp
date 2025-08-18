class Solution {
public:
    int mySqrt(int x) {
        if(x==0) return 0;
        long long g=x;
        while(g*g>x){
            g=(g+x/g)/2;
        }
        return (int)g;
    }
};