import { useMapStore } from "./Store";
export function Popup({ title, text, row1 = null, row2 = null, row3 = null }) {
  const closePopup = useMapStore((state) => state.closePopup);
  return (
    <div className="map-popup">
      <div className="map-popup__close" onClick={closePopup}>
        Fermer ×
      </div>
      <h3>{title}</h3>
      <p>{text}</p>
      {row1 && (
        <p>
          {row1[0]} : <strong>{row1[1]}</strong>
        </p>
      )}
      {row2 && (
        <p>
          {row2[0]} : <strong>{row2[1]}</strong>
        </p>
      )}
      {row3 && (
        <p>
          {row3[0]} : <strong>{row3[1]}</strong>
        </p>
      )}
    </div>
  );
}
