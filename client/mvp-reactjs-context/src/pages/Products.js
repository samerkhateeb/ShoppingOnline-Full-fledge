import "./Products.css";

import React, { useContext, useState } from "react";

import { Button } from "react-bootstrap";
import Card from "../components/Card";
import InputField from "../controls/InputField";
import ShopContext from "../context/shop-context";

// import { connect } from "react-redux";
function ProductsPage(props) {
  const context = useContext(ShopContext);
  const [newPanel, setNewPanel] = useState();
  const [title, setTitle] = useState("");
  const [cost, setCost] = useState("");
  const [description, setDescription] = useState("");
  const [amount, setAmount] = useState("");

  const updateHandler = (data) => {
    context.doProductUpdate(data);
  };
  const deleteHandler = async (data) => {
    await context.doProductDelete(data);
  };

  const resetNewPanel = () => {
    setNewPanel(false);
    setTitle("");
    setCost("");
    setDescription("");
    setAmount("");
  };

  const newHandler = (e) => {
    e.preventDefault();
    const product_data = {
      title: title,
      description: description,
      cost: cost,
      amount: amount,
      category: 3,
    };
    let data = product_data;
    resetNewPanel();
    context.doProductNew(data);
  };
  return (
    <>
      <main className="products">
        {context.user_type === "2" && (
          <div>
            <Button
              as="a"
              variant="primary"
              onClick={() => {
                setNewPanel(true);
              }}
            >
              New Product
            </Button>

            {newPanel && (
              <div>
                <form onSubmit={newHandler}>
                  <InputField title="Title" value={title} onChange={setTitle} />
                  <InputField
                    title="Description"
                    value={description}
                    small="Description field should describe your product details like the size  of the product and the status of the product is it new or not"
                    onChange={setDescription}
                  />
                  <InputField title="Cost $$" value={cost} onChange={setCost} />
                  <InputField
                    title="Amount"
                    value={amount}
                    onChange={setAmount}
                  />
                  <Button variant="primary m-2" type="submit">
                    Save
                  </Button>
                  <Button
                    variant="primary m-2"
                    type="button"
                    onClick={(e) => {
                      setNewPanel(false);
                    }}
                  >
                    Cancel
                  </Button>
                </form>
              </div>
            )}
          </div>
        )}
        <ul>
          {context.products.map((product) => (
            <Card
              product={product}
              context={context}
              onUpdateSubmit={(data) => {
                updateHandler(data);
              }}
              onDeleteSubmit={(data) => {
                deleteHandler(data);
              }}
            />
          ))}
        </ul>
      </main>
    </>
  );
}

// const mapStateToProps = (state) => {
//   return {
//     products: state.products,
//     cartItemCount: state.cart.reduce((count, curItem) => {
//       return count + curItem.quantity;
//     }, 0),
//   };
// };

// const mapDispatchToProps = (dispatch) => {
//   return {
//     addProductToCart: (product) => dispatch(addProductToCart(product)),
//   };
// };

// // connect the component with the global redux store
// export default connect(
//   mapStateToProps,
//   mapDispatchToProps
// )(ProductsPage);

export default ProductsPage;