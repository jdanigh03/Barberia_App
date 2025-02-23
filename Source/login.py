import flet as ft

def main(page: ft.Page):
    page.title = "Login Barbería"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Imagen que se mostrará arriba del formulario de login
    imagen_barberia = ft.Image(
        src="../imagenes/peluqueria.png",  
        width=200,
        height=200,
        fit="contain"
    )

    # Campos de texto para usuario y contraseña
    txt_usuario = ft.TextField(label="Usuario", width=300)
    txt_contraseña = ft.TextField(label="Contraseña", width=300, password=True, can_reveal_password=True)

    # Función para cerrar el diálogo
    def cerrar_dialog(e):
        page.dialog.open = False
        page.update()

    # Función para validar el login
    def iniciar_sesion(e):
        if txt_usuario.value == "admin" and txt_contraseña.value == "admin":
            dlg = ft.AlertDialog(
                title=ft.Text("Acceso Correcto"),
                content=ft.Text("Bienvenido a la Barbería"),
                actions=[ft.TextButton("Cerrar", on_click=cerrar_dialog)]
            )
        else:
            dlg = ft.AlertDialog(
                title=ft.Text("Acceso Incorrecto"),
                content=ft.Text("Usuario o contraseña incorrectos"),
                actions=[ft.TextButton("Cerrar", on_click=cerrar_dialog)]
            )
        page.dialog = dlg
        dlg.open = True
        page.update()

    btn_login = ft.ElevatedButton(text="Iniciar Sesión", on_click=iniciar_sesion)

    # Agregamos la imagen y los demás controles a la página
    page.add(
        imagen_barberia,
        txt_usuario,
        txt_contraseña,
        btn_login
    )

# Ejecutamos la aplicación, en este ejemplo simulamos una pantalla móvil de 360x640
ft.app(target=main)
