function FourierVisualization()
    % 1. Cria a figura principal
    fig = figure('Name', 'Serie de Fourier', 'Position', [100, 100, 500, 400]);

    % 2. Cria os eixos para o gráfico
    ax = axes('Parent', fig, 'Position', [0.1, 0.2, 0.8, 0.7]);

    % 3. Cria o botão deslizante (slider)
    % Estilo 'slider', valor inicial 1, variando de 0.1 a 10
    h_slider = uicontrol('Style', 'slider',
                         'Parent', fig,
                         'Min', 0.05, 'Max', 1, 'Value', 0.1,
                         'Position', [50, 20, 400, 20],
                         'sliderStep', [0.05, 0.05],
                         'Callback', @atualiza_grafico);

    % 4. Cria um texto para mostrar o valor atual do slider
    h_texto = uicontrol('Style', 'text', 'Parent', fig,
                        'Position', [225, 5, 50, 15], 'String',
                        num2str(get(h_slider, 'Value')));
    nf = 40;
    % 5. Plota a linha inicial
    n = 0:nf;
    omega = get(h_slider, 'Value');
    x = cos(0.5 * n);
    stem(ax, n, x, 'LineWidth', 2, 'b');
    hold on;
    y = cos(omega * n);
    linha = stem(ax, n, y, 'LineWidth', 2, 'r');

    xlim(ax, [0, nf+1]);
    ylim(ax, [-1.2, 1.2]);

    % 6. Função de Callback (acionada ao mover o slider)
    function atualiza_grafico(~, ~)
        % Lê o valor atual do slider
        omega = get(h_slider, 'Value');

        % Atualiza os dados do gráfico (mais eficiente que usar 'plot' novamente)
        y_novo = cos(omega * n);
        set(linha, 'YData', y_novo);

        % Atualiza o texto com o valor formatado
        set(h_texto, 'String', sprintf('%.2f', omega));

        % Força o Octave a redesenhar a janela
        drawnow;
    end
end

