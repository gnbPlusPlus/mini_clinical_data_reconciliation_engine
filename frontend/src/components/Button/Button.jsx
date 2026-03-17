import './Button.css';

export default function Button({ onClick, children }) {
    return (
        <button className="custom_button" onClick={onClick}>
            {children}
        </button>
    );
}