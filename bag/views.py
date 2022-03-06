from django.shortcuts import render, redirect


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    # if a product with a size has been added
    if size:
        # check if an item with the same id and size is already in the bag, if so increment for that size
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                # if the item is in the bag, but thias is a new size add to the bag
                bag[item_id]['items_by_size'][size] = quantity
        # if the item is not already in the bag, add the item
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        # if the item has no size
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
    