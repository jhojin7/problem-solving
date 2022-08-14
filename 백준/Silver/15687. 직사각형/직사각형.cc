class Rectangle{
    private:
        int width;
        int height;
    public:
        Rectangle(int w, int h){
            width = w;
            height = h;
        };
        int get_width() const {return width;}
        int get_height() const {return height;}
        void set_width(int w){
            if (w<=0 or w>1000) return;
            width = w;
        }
        void set_height(int h){
            if (h<=0 or h>2000) return;
            height = h;
        }
        int area() const {return width*height;}
        int perimeter() const {return 2*(width+height);}
        bool is_square() const {return width==height;}
};